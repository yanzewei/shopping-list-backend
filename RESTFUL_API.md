# RESTFUL API

## Get shopping cart's qunatity by user id.

```
Action: api/shopquantity/<int:uid>
Method: Get
Return: {'status': 'success', 'data': {"quantity":quantity}}, 200
```

## Get or search the products

```
Action: api/product/<title>?
Parameter: According the title to search. If the title is null, then it will return all the products.
Method: Get
Return: {'status': 'success', 'data': result}, 200

result looks like:
{
  game_machine: [{brand_id: 18, id: 1, category: 2, remain_count: 97, price: 666, brand_name: "IGT", logo:"xxx.png"},…]
  phones: [{brand_id: 1, id: 1, category: 1, remain_count: 17, price: 1992, brand_name: "Apple", logo:"yyy.jpg"},…]
}
```

## Get shopping list by user id

```
Action: api/shoplist/<int:uid>
Method: Get
Return: {'status': 'success', 'data': result}, 200

result looks like:
[{num: 12, brand_id: 10, id: 10, category: 1, remain_count: 12, price: 1312, brand_name: "Doro", num: 12, logo: "xxx.jpg"},…]

```

## Add item to the shopping cart

```
Action: api/shoplist
Method: Post
Parameters: {key: "2-1", nums: 1, remain_count: "97", uid: 1}
the parameter key means category_id-subcategory-id
Return: 
when success: { "status": 'success'}, 201 
when fail:
{'message': 'detail message'}, 400|422
```

## Update item numbers in the shopping cart

```
Action: api/shoplist
Method: Put
Parameters: {key: "2-1", nums: 1, remain_count: "97", uid: 1}
the parameter key means category_id-subcategory-id
Return: 
when success: { "status": 'success'}, 200 
when fail:
{'message': 'detail message'}, 400|422
```

## Delete item from the shopping cart

```
Action: api/shoplist
Method: Delete
Parameters: {key: "2-1",  uid: 1}
the parameter key means category_id-subcategory-id
Return: 
when success: { "status": 'success'}, 200 
when fail:
{'message': 'detail message'}, 400|422
```



