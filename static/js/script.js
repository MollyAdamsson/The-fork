window.onload = () => {
    let manageBookingsElement = document.querySelector('#manage-bookings');
    let modal = manageBookingsElement.querySelector('#exampleModal');
    let buttons = manageBookingsElement.querySelectorAll('.delete-button');
    buttons.forEach((item) => {
        item.addEventListener('click',() => {
            modal.dataset.id = item.dataset.id;
        });
    })

    let confirmationButton = modal.querySelector('#confirmDeleteButton');
    confirmationButton.addEventListener('click', () => {
        window.location.href = modal.dataset.deleteUrl + '/?bookingId=' + modal.dataset.id; 
    })
};