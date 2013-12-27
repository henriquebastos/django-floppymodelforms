# -*- coding: utf-8 -*-
from django.test import TestCase
from django.forms.models import modelform_factory
from django.contrib.auth.models import User
from floppyforms import fields as floppyfields


class TestFloppyModelForms(TestCase):
    def setUp(self):
        form_class = modelform_factory(User)
        self.form = form_class()

    def test_floppy_fields(self):
        floppyfields_count = 0

        for f in self.form.fields.values():
            field_name = f.__class__.__name__
            if hasattr(floppyfields, field_name):
                self.assertIsInstance(f, getattr(floppyfields, field_name))
                floppyfields_count += 1

        self.assertEqual(10, floppyfields_count)
