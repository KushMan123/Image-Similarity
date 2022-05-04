const innerBars = document.querySelectorAll(".bar-inner");
const image1 = document.getElementById("image1");
const image2 = document.getElementById("image2");
const image3 = document.getElementById("image3");
const root = document.documentElement;
//Horizontal Charts
innerBars.forEach((bar) => {
	bar.style.width = bar.dataset.percent;
});
// Circular Charts
function changeChartNumber(percent, number) {
	let valueNumber = parseInt(472 - (472 * percent) / 100);
	console.log(percent, valueNumber);
	let counter = 0;
	root.style.setProperty("--end-dashstroke", valueNumber);
	setInterval(() => {
		if (counter == percent) {
			clearInterval;
		} else {
			counter += 1;
			number.innerHTML = `${counter}%`;
		}
	}, 30);
}
image1.addEventListener("mouseenter", function () {
	let number = document.querySelector("#image1 .number");
	let percent = parseInt(number.dataset.percent);
	changeChartNumber(percent, number);
});

image2.addEventListener("mouseenter", function () {
	let number = document.querySelector("#image2 .number");
	let percent = parseInt(number.dataset.percent);
	changeChartNumber(percent, number);
});

image3.addEventListener("mouseenter", function () {
	let number = document.querySelector("#image3 .number");
	let percent = parseInt(number.dataset.percent);
	changeChartNumber(percent, number);
});

// Befor Image Uploaded

const defaultBtn = document.getElementById("default-btn");
const customBtn = document.getElementById("custom-btn");
const cancelBtn = document.getElementById("cancel-btn");
const img = document.querySelector(".outer-wrapper .image img");
const fileName = document.querySelector(".file-name");
const modelBtn = document.getElementById("model-btn");
const wrapper = document.querySelector(".outer-wrapper");
const wrapperContainer = document.querySelector(".wrapper-container");
const outerContainer = document.querySelector(".outer-container");

var hasUploaded = false;

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
			hasUploaded = false;
		});
		reader.readAsDataURL(file);
		hasUploaded = true;
	}
	if (this.value) {
		let valueStore = this.value.match(regExp);
		fileName.textContent = valueStore;
	}
});

modelBtn.addEventListener("click", () => {
	if (hasUploaded) {
		outerContainer.style.display = "none";
		wrapperContainer.style.display = "none";
		customBtn.style.display = "none";
		modelBtn.style.display = "none";
	}
});
