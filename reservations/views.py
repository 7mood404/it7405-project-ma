from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reservation


@login_required
def reserve_table(request):
    if request.method == 'POST':
        Reservation.objects.create(
            user=request.user,
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            people=request.POST.get('people'),
        )
        return redirect('my_reservations')

    return render(request, 'reservations/reserve.html')


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'reservations/my_reservations.html', {'reservations': reservations})


# ✅ ADD THIS (do not remove the others)
@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(
        Reservation,
        id=reservation_id,
        user=request.user
    )

    # Only allow cancel if still pending
    if reservation.status == 'Pending':
        reservation.status = 'Cancelled'
        reservation.save()

    return redirect('my_reservations')