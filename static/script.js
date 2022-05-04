const defaultBtn = document.getElementById("default-btn");
const customBtn = document.getElementById("custom-btn");
const cancelBtn = document.getElementById("cancel-btn");
const img = document.querySelector(".wrapper .image img");
const fileName = document.querySelector(".file-name");
const wrapper = document.querySelector(".wrapper");
const modelBtn = document.getElementById("model-btn");
const body = document.querySelector(".body");

let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;

function defaultBtnActive() {
	defaultBtn.click();
}

defaultBtn.addEventListener("change", function () {
	const file = this.files[0];
	if (file) {
		reader = new FileReader();
		reader.onload = function () {
			const result = reader.result;
			img.src = result;
			wrapper.classList.add("active");
		};
		cancelBtn.addEventListener("click", function () {
			img.src = "";
			wrapper.classList.remove("active");
		});
		reader.readAsDataURL(file);
	}
	if (this.value) {
		let valueStore = this.value.match(regExp);
		fileName.textContent = valueStore;
	}
});

function modelBtnClick() {
	body.classList.add("grid");
}
