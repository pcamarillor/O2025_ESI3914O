# Data Generator for Dyomorphos
from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

class DyomorphosDataGenerator:
    """
    Generates synthetic e-commerce data for Dyomorphos clothing brand.
    Products: T-shirts, Caps, Coats
    """
    
    def __init__(self, num_customers=500, num_orders=2000):
        self.num_customers = num_customers
        self.num_orders = num_orders
        
        # Dyomorphos product catalog
        self.products = [
            # T-shirts
            {'product_id': 1, 'product_name': 'Classic Cotton Tee', 'category': 'T-Shirt', 'price': 29.99, 'sizes': ['XS', 'S', 'M', 'L', 'XL', 'XXL']},
            {'product_id': 2, 'product_name': 'Graphic Print Tee', 'category': 'T-Shirt', 'price': 34.99, 'sizes': ['S', 'M', 'L', 'XL', 'XXL']},
            {'product_id': 3, 'product_name': 'Premium V-Neck Tee', 'category': 'T-Shirt', 'price': 39.99, 'sizes': ['S', 'M', 'L', 'XL']},
            {'product_id': 4, 'product_name': 'Oversized Street Tee', 'category': 'T-Shirt', 'price': 44.99, 'sizes': ['M', 'L', 'XL', 'XXL']},
            {'product_id': 5, 'product_name': 'Long Sleeve Tee', 'category': 'T-Shirt', 'price': 42.99, 'sizes': ['S', 'M', 'L', 'XL']},
            
            # Caps
            {'product_id': 6, 'product_name': 'Classic Snapback Cap', 'category': 'Cap', 'price': 24.99, 'sizes': ['One Size']},
            {'product_id': 7, 'product_name': 'Embroidered Dad Cap', 'category': 'Cap', 'price': 27.99, 'sizes': ['One Size']},
            {'product_id': 8, 'product_name': 'Trucker Mesh Cap', 'category': 'Cap', 'price': 22.99, 'sizes': ['One Size']},
            {'product_id': 9, 'product_name': 'Vintage Baseball Cap', 'category': 'Cap', 'price': 26.99, 'sizes': ['One Size']},
            
            # Coats
            {'product_id': 10, 'product_name': 'Winter Puffer Coat', 'category': 'Coat', 'price': 189.99, 'sizes': ['S', 'M', 'L', 'XL', 'XXL']},
            {'product_id': 11, 'product_name': 'Denim Jacket', 'category': 'Coat', 'price': 129.99, 'sizes': ['S', 'M', 'L', 'XL']},
            {'product_id': 12, 'product_name': 'Windbreaker Jacket', 'category': 'Coat', 'price': 89.99, 'sizes': ['S', 'M', 'L', 'XL', 'XXL']},
            {'product_id': 13, 'product_name': 'Fleece Zip Hoodie', 'category': 'Coat', 'price': 79.99, 'sizes': ['XS', 'S', 'M', 'L', 'XL']},
            {'product_id': 14, 'product_name': 'Varsity Bomber Jacket', 'category': 'Coat', 'price': 159.99, 'sizes': ['S', 'M', 'L', 'XL']},
        ]
        
        self.colors = ['Black', 'White', 'Navy', 'Gray', 'Olive', 'Burgundy', 'Charcoal']
        
    def generate_customers(self):
        """Generate customer data"""
        customers = []
        for i in range(self.num_customers):
            customers.append({
                'customer_id': i + 1,
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'email': fake.email(),
                'phone': fake.phone_number(),
                'street_address': fake.street_address(),
                'city': fake.city(),
                'state': fake.state_abbr(),
                'zip_code': fake.zipcode(),
                'country': 'USA',
                'registration_date': fake.date_between(start_date='-2y', end_date='-30d').isoformat(),
                'loyalty_member': random.choice([True, False])
            })
        return pd.DataFrame(customers)
    
    def generate_products(self):
        """Generate product catalog with variants"""
        product_variants = []
        variant_id = 1
        
        for product in self.products:
            base_stock = random.randint(20, 150)
            
            for size in product['sizes']:
                for color in random.sample(self.colors, k=random.randint(3, 5)):
                    product_variants.append({
                        'variant_id': variant_id,
                        'product_id': product['product_id'],
                        'product_name': product['product_name'],
                        'category': product['category'],
                        'size': size,
                        'color': color,
                        'price': product['price'],
                        'stock_quantity': random.randint(0, base_stock),
                        'sku': f"DYO-{product['product_id']:03d}-{size}-{color[:3].upper()}"
                    })
                    variant_id += 1
        
        return pd.DataFrame(product_variants)
    
    def generate_orders(self, customers_df, products_df):
        """Generate orders and order items"""
        orders = []
        order_items = []
        
        for i in range(self.num_orders):
            customer_id = random.choice(customers_df['customer_id'].tolist())
            order_date = fake.date_time_between(start_date='-1y', end_date='now')
            
            # Order status with realistic distribution
            status = random.choices(
                ['completed', 'pending', 'shipped', 'cancelled', 'processing'],
                weights=[0.65, 0.08, 0.15, 0.07, 0.05]
            )[0]
            
            order_id = i + 1
            
            # Discount code (10% of orders)
            discount_code = random.choice([None, None, None, None, None, None, None, None, None, 'WELCOME10']) if random.random() < 0.1 else None
            discount_amount = 0
            
            orders.append({
                'order_id': order_id,
                'customer_id': customer_id,
                'order_date': order_date.isoformat(),
                'status': status,
                'payment_method': random.choice(['credit_card', 'debit_card', 'paypal', 'apple_pay']),
                'discount_code': discount_code,
                'shipping_cost': 0 if random.random() < 0.3 else 7.99  # Free shipping sometimes
            })
            
            # Generate 1-4 items per order (weighted towards 1-2 items)
            num_items = random.choices([1, 2, 3, 4], weights=[0.5, 0.3, 0.15, 0.05])[0]
            selected_variants = random.sample(products_df['variant_id'].tolist(), min(num_items, len(products_df)))
            
            order_total = 0
            for variant_id in selected_variants:
                variant = products_df[products_df['variant_id'] == variant_id].iloc[0]
                quantity = random.randint(1, 2)  # Usually 1, sometimes 2
                unit_price = variant['price']
                subtotal = round(unit_price * quantity, 2)
                
                order_items.append({
                    'order_item_id': len(order_items) + 1,
                    'order_id': order_id,
                    'variant_id': variant_id,
                    'product_name': variant['product_name'],
                    'category': variant['category'],
                    'size': variant['size'],
                    'color': variant['color'],
                    'quantity': quantity,
                    'unit_price': unit_price,
                    'subtotal': subtotal
                })
                order_total += subtotal
            
            # Apply discount if applicable
            if discount_code:
                discount_amount = round(order_total * 0.1, 2)
            
            # Update order with total
            orders[-1]['subtotal'] = round(order_total, 2)
            orders[-1]['discount_amount'] = discount_amount
            orders[-1]['total_amount'] = round(order_total - discount_amount + orders[-1]['shipping_cost'], 2)
        
        return pd.DataFrame(orders), pd.DataFrame(order_items)
    
    def save_data(self, output_dir):
        """Generate and save all datasets"""
        print("=" * 60)
        print("DYOMORPHOS DATA GENERATOR")
        print("=" * 60)
        
        print("\n[1/3] Generating customers...")
        customers_df = self.generate_customers()
        customers_df.to_csv(f"{output_dir}/customers.csv", index=False)
        print(f"✓ Generated {len(customers_df)} customers")
        
        print("\n[2/3] Generating product catalog...")
        products_df = self.generate_products()
        products_df.to_csv(f"{output_dir}/products.csv", index=False)
        print(f"✓ Generated {len(products_df)} product variants")
        print(f"  - T-Shirts: {len(products_df[products_df['category'] == 'T-Shirt'])}")
        print(f"  - Caps: {len(products_df[products_df['category'] == 'Cap'])}")
        print(f"  - Coats: {len(products_df[products_df['category'] == 'Coat'])}")
        
        print("\n[3/3] Generating orders and order items...")
        orders_df, order_items_df = self.generate_orders(customers_df, products_df)
        orders_df.to_csv(f"{output_dir}/orders.csv", index=False)
        order_items_df.to_csv(f"{output_dir}/order_items.csv", index=False)
        print(f"✓ Generated {len(orders_df)} orders")
        print(f"✓ Generated {len(order_items_df)} order items")
        
        # Summary statistics
        total_revenue = orders_df[orders_df['status'] == 'completed']['total_amount'].sum()
        print("\n" + "=" * 60)
        print("DATASET SUMMARY")
        print("=" * 60)
        print(f"Total Revenue (Completed Orders): ${total_revenue:,.2f}")
        print(f"Average Order Value: ${orders_df['total_amount'].mean():.2f}")
        print(f"Date Range: {orders_df['order_date'].min()} to {orders_df['order_date'].max()}")
        print("\nFiles saved to:", output_dir)
        print("=" * 60)

# Usage example
if __name__ == "__main__":
    generator = DyomorphosDataGenerator(num_customers=500, num_orders=2000)
    generator.save_data("/home/linguini/O2025_ESI3914O/spark/data/ecommerce")