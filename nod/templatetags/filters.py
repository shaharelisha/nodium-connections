import calendar
import datetime

from django import template
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, FieldDoesNotExist
from django.utils import timezone

from nod.models import *

register = template.Library()


@register.filter(name="role")
def get_role(user):
    role_name = next(name for value, name in StaffMember.ROLES if value==user.staffmember.role)
    return role_name


@register.filter(name='address')
def get_full_address(customer):
    return customer.full_address()


@register.filter(name='phones')
def get_all_phones(customer):
    return customer.get_phones()


@register.filter(name='emails')
def get_all_email(customer):
    return customer.list_emails()


@register.filter(name='is_business')
def is_business(customer):
    if customer.__class__.__name__ == "BusinessCustomer":
        return True
    else:
        return False


@register.filter(name='job_tasks')
def get_tasks(invoice):
    return invoice.job_done.tasks.filter(is_deleted=False)


@register.filter(name='job_parts')
def get_job_parts(invoice):
    return invoice.job_done.parts.filter(is_deleted=False)


@register.filter(name='price')
def get_markedup_price(part):
    return part.get_markedup_price()


@register.filter(name='total_cost')
def get_cost(part):
    return part.part.get_markedup_price() * part.quantity


@register.filter(name='labour_duration')
def get_duration(job):
    return job.get_duration()


@register.filter(name='labour_price')
def get_labour_price(job):
    return job.get_labour_price()


@register.filter(name='total')
def get_total_price(job):
    return job.get_price()


@register.filter(name='vat')
def get_vat(job):
    return job.get_vat()


@register.filter(name='grand_total')
def get_grand_total(job):
    return job.get_grand_total()

# @register.filter(name='vehicle_reg_num')
# def get_vehicle(invoice):
#     return invoice.job_done.vehicle.reg_number
#
#
# @register.filter(name='vehicle_make')
# def get_vehicle(invoice):
#     return invoice.job_done.vehicle.make
#
#
# @register.filter(name='vehicle_model')
# def get_vehicle(invoice):
#     return invoice.job_done.vehicle.model