
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,RequestContext,render
from .models import *
from django.db.models import Q
import re
import random
import datetime
from django.core.mail import send_mail,EmailMessage












