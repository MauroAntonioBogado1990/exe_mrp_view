{
    'name': 'Exe MRP View',
    'version': '17.0',
    'category': 'Tools',
    'author':'Mauro Bogado,Exemax',
    'summary': 'Modulo para retornar la vista de tablet de manera correcta',
    'depends': ['base','sale', 'account', 'mrp'],
    'data': [
        #'security/ir.model.access.csv',
        
        'views/exe_mrp_view.xml',
    ],

    'installable': True,
    'application': False,
}   