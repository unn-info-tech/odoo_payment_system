{
    'name': 'Educational Payment System',
    'version': '1.0',
    'sequence': -400,
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',  
        'views/course_views.xml',
        'views/teacher_views.xml',
        'views/student_views.xml',
        'views/group_views.xml',
        'views/payment_views.xml',
        'views/salary_payment_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,

}
