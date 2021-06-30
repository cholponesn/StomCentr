from django.urls import path
from .views import *

urlpatterns = [
    path('',DayViewSet.as_view({
                                'get':'list',
    'post':'create',}),name='day'),
    path('day/<int:day_id>/', DayViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }),name='day_detail'),
    path('work_days/',DoctorDayView.as_view({
        'get':'list'})),
    path('work_days/<int:day_id>/', DoctorDayView.as_view({
        'post':'create'

        })),
    path('modify_wd/<int:doctor_day_id/',DoctorDayView.as_view({
        'put':'update',
        'get':'retrieve'

    }))


]