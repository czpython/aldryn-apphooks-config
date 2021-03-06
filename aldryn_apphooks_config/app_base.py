# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from cms.app_base import CMSApp


class CMSConfigApp(CMSApp):

    def get_configs(self):
        return self.app_config.objects.all()

    def get_config(self, namespace):
        try:
            return self.app_config.objects.get(namespace=namespace)
        except ObjectDoesNotExist:
            return None

    def get_config_add_url(self):
        try:
            return reverse('admin:%s_%s_add' % (self.app_config._meta.app_label,
                                                self.app_config._meta.model_name))
        except AttributeError:  #NOQA
            return reverse('admin:%s_%s_add' % (self.app_config._meta.app_label,
                                                self.app_config._meta.module_name))