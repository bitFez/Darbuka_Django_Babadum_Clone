var correct_popup;
var incorrect_popup;

window.addEventListener('load', () => {
	correct_popup = document.querySelector('.correct-popup');
	incorrect_popup = document.querySelector('.incorrect-popup');
});

// Correct Answer:
window.addEventListener('correct-answer', () => {
	correct_popup.classList.add('main-popup-visible');
	setTimeout(() => {
		window.location.reload();
	}, 1000);
});

// Incorrect Answer:
window.addEventListener('incorrect-answer', () => {
	incorrect_popup.classList.add('main-popup-visible');
	setTimeout(() => {
		window.location.reload();
	}, 3000);
});