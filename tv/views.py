from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import random

class ChannelsListView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = 'TV/list_channels.html'
		categories = Category.objects.filter()

		request.user.profile.update_status()
		
		ListOfChannelsByCategory = []

		for category in categories:
			ListOfChannelsByCategory.append({'category': category.name, 'channels': Channel.objects.filter(category=category, link_status="Functional")})

		context = {
			'ListOfChannelsByCategory': ListOfChannelsByCategory,
		}
		return render(request, template_name, context)

class ChannelDetailView(View):
	@method_decorator(login_required)
	def get(self, request, slug):
		template_name = 'TV/detail_channel.html'
		channel = get_object_or_404(Channel, slug=slug)
		category = Category.objects.get(pk=channel.category.pk)
		similarChannels = Channel.objects.filter(category=category, link_status="Functional").exclude(pk=channel.pk)
		listChannels = list(similarChannels)

		if len(listChannels) < 6:
			randomChannels = random.sample(listChannels, len(listChannels))
		else:
			randomChannels = random.sample(listChannels, 6)

		context = {
			'channel': channel,
			'category': category,
			'randomChannels': randomChannels,
		}
		return render(request, template_name, context)