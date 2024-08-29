{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Manage school subjects, students, and teachers',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/subject_views.xml',
        'views/teacher_views.xml',
        'data/menu_items.xml',
    ],
    'installable': True,
    'application': True,
}