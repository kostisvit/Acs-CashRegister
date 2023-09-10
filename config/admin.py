from tameiaki.admin import CashAdmin
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from accounts.models import CustomUser
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

from tameiaki.models import Cash
from accounts.admin import CustomUserAdmin

class OTPAdmin(OTPAdminSite):
    pass


admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(CustomUser,CustomUserAdmin)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)
admin_site.register(Cash,CashAdmin)