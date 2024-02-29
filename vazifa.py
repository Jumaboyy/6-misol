import psycopg2 as sql

db = sql.connect(
    database='avtosalon',
    host='localhost',
    user='postgres',
    password='2004',
    port='5432'
)
cursor = db.cursor()

# cursor.execute('''SELECT model_name,brand_id,color_id  FROM models''')
# models = cursor.fetchall()
# res=[]
# for model in models:
#     berand_id=model[1]
#     color_id=model[2]
#     cursor.execute(f"SELECT brand_name FROM brands WHERE brand_id={berand_id}")
#     brand = cursor.fetchone()
#     cursor.execute(f"SELECT color_name FROM colors WHERE color_id={color_id}")
#     color = cursor.fetchone()
#     print({
#         'model_name': model[0],
#     'brand_name': brand[0],
#     'color_name': color[0]
# });


# cursor.execute(f"SELECT email FROM customers")
# email1=cursor.fetchall()
# print(email1)
# cursor.execute(f"SELECT email FROM employees")
# email2=cursor.fetchall()
# print(email2)


cursor.execute(f'''Select country, count(customer_id) from customers GROUP BY country''')

country=cursor.fetchall()
# print(country)
for i in country:
    print(i)