# -*- coding: utf-8 -*-
from odoo import models, fields, api

# This is the main model for our Student Management module.
class Student(models.Model):
    _name = 'student.management'
    _description = 'Student'

# Define the fields for our student model
    name = fields.Char(
        string='Student Name',
        required=True,
        help='Full name of the student'
    )

    email = fields.Char(
        string='Email',
        help='Student email address'
    )

    phone = fields.Char(
        string='Phone',
        help='Contact number'
    )

    date_enrolled = fields.Date(
        string='Enrollment Date',
        default=fields.Date.today,
        help='Date when the student was enrolled'
    )

    active = fields.Boolean(
        string='Active',
        default=True,
        help='If unchecked, the student will be hidden from lists (soft delete)'
    )

    notes = fields.Text(
        string='Notes',
        help='Any additional notes about the student'
    )
# API methods for external access
    @api.model
    def api_get_students(self, active_only=True):
        domain = [('active', '=', True)] if active_only else []
        students = self.search_read(
            domain,
            ['id', 'name', 'email', 'phone', 'date_enrolled'],
            order='name'
        )
        return students

    @api.model
    def api_create_student(self, vals):
        return self.create(vals).id

    @api.model
    def api_get_student(self, student_id):
        student = self.browse(student_id).exists()
        if not student:
            return False
        return student.read(['id', 'name', 'email', 'phone', 'date_enrolled', 'notes', 'active'])[0]
    
    @api.model
    def api_update_student(self, student_id, vals):
        student = self.browse(student_id).exists()
        if not student:
            return False
        student.write(vals)
        return True

    @api.model
    def api_delete_student(self, student_id):
        student = self.browse(student_id).exists()
        if not student:
            return False
        student.unlink()
        return True

