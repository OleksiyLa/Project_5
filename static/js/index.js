let toasts = document.getElementsByClassName('custom-toast');
if(toasts) {
    toasts = Array.from(toasts);
    toasts.forEach(toast => {
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
    });
}
