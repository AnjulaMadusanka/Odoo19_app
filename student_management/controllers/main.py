# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class StudentAPI(http.Controller):
    #fetch students data using API
    @http.route('/api/students', type='json', auth='public', methods=['POST'], csrf=False)
    def get_students(self, active_only=True):
        students = request.env['student.management'].sudo().api_get_students(active_only)
        return {
            'status': 'success',
            'data': students
        }
    #create student data using API
    @http.route('/api/students/create', type='json', auth='public', methods=['POST'], csrf=False)
    def create_student(self, **kwargs):
        if not kwargs.get('name'):
            return {
                'status': 'error',
                'message': 'Student name is required'
            }
        
        student_id = request.env['student.management'].sudo().api_create_student(kwargs)

        return {
            'status': 'success',
            'student_id': student_id
        }
    
    #update student data using API
    @http.route('/api/students/update', type='json', auth='public', methods=['POST'], csrf=False)
    def update_student(self, **kwargs):

        student_id = kwargs.pop('student_id', None)
        if not student_id:
            return {
                'status': 'error',
                'message': 'student_id is required'
            }

        success = request.env['student.management'].sudo().api_update_student(student_id, kwargs)

        if not success:
            return {
                'status': 'error',
                'message': 'Student not found or update failed'
            }

        return {
            'status': 'success',
            'student_id': student_id
        }
    
    #Delete student data using API
    @http.route('/api/students/delete', type='json', auth='public', methods=['POST'], csrf=False)
    def delete_student(self, **kwargs):
      
        student_id = kwargs.get('student_id')
        if not student_id:
            return {
                'status': 'error',
                'message': 'student_id is required'
            }

        success = request.env['student.management'].sudo().api_delete_student(student_id)

        if not success:
            return {
                'status': 'error',
                'message': 'Student not found or delete failed'
            }

        return {
            'status': 'success',
            'student_id': student_id
        }

