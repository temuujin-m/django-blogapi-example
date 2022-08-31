# class noift(APIView):
#     def post(self, request):

#         user = User.objects.filter(id=2)
#         print(type(user))
#         device = FCMDevice.objects.get(user_id=8)
#         registration_token = device.registration_id
#         print(type(device))
#         print(registration_token)

#         # if device is user: 
#         message = Message(
#             notification=Notification(
#                 title='ㅁ1ㅁ2ㅁ', 
#                 body='ㅇ3ㅇ4ㅇ'
#             )

#         )
        
#         response = device.send_message(message)
#         print('Success', response)
#         return HttpResponse(response)


# user_id = User.objects.get(id=request.data['user_id'])
# device = FCMDevice()
# device = FCMDevice.objects.get(user_id)
# print(device)

# class Notification(View):
#     def post(self, request, *args, **kwargs):
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         push = request.POST.get('push')

#         if push:
#             message = Message(
#                 notification=Notification(
#                     title=title,
#                     body=content
#                 )
#             )
#             try:
#                 devices = FCMDevice.objects.filter(user_id=['2'])
#                 devices.send_message(message)
#             except Exception as e:
#                 print('Push notification failed', e)
            
#         return HttpResponse(reverse('notice_list'))


