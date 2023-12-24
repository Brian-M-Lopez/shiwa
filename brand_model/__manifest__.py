{
    'name': 'Product brand and model',
    'version': '16.0.0.1',
    'description': 'Add to each product and product template a brand and a model ',
    'author': 'Brian Misael Lopez',
    'license': 'LGPL-3',
    'depends': [
        'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/brand.xml',
        'views/model.xml',
        'views/product_views.xml',
    ],
    'application': False,
}