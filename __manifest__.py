{
    "name": "HMS",
    "version": "1.0",
    "summary": "Manages hospital systems.",
    "description": "A comprehensive module for managing hospital, doctors and patiants.",
    "category": " ",
    "author": "Luka",
    "depends": ["base"],
    "data": [
        "security/hms_security.xml",
        "security/ir.model.access.csv",
        "views/hms_patient_view.xml",
        "views/hms_doctor_view.xml",
        "views/hms_department_view.xml",
        "views/hms_partner_view.xml",
        "views/hms_menu_view.xml"
    ],
    "application": True,
    "installable": True,
    "license": "LGPL-3",
}