#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015/12/20
# @Author  : chex
from django.shortcuts import render_to_response

__title__ = ''

def index(request):
	template_name = 'index.html'
	return render_to_response(template_name)