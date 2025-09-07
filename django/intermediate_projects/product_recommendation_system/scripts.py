import django
import pandas as pd
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'recommend.settings'
django.setup()
from home.models import Product
import time
import csv
csv_file_path='flipkart_com-ecommerce_sample.csv'

with open(csv_file_path,mode='r',encoding='utf-8') as file:
    reader=csv.DictReader(file)

    for row in reader:
        try:
            product_name=row['product_name']
            product_image=eval(row['image'])[0] #first image from the list
            description=row['description']
            category=row['product_category_tree'].split('>>')[0].strip('[]"') #Extract last category
            price=row['retail_price']

            print(product_name,product_image,description,category,price)

            # time.sleep(1)

            #Create or update product
            Product.objects.update_or_create(
                name=product_name,
                defaults={
                    'product_image':product_image,
                    'description':description,
                    'category':category,
                    'price':price
                }
            )
        except Exception as e:
            print(e)

print("Products imported successfully.")


