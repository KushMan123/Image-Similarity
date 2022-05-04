import React, { useEffect, useRef, useState } from "react";
import Button from "./Button";

let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;

const ImageUpload = (props) => {
	const { handleFunction, handleStatus } = props;
	const [imageSrc, setImageSrc] = useState(" ");
	const wrapperRef = useRef();
	const fileRef = useRef();
	const defaultBtnRef = useRef();

	useEffect(() => {
		if (imageSrc !== " ") {
			handleStatus(true);
		}
	}, [imageSrc]);

	function handleDefaultClick(e) {
		const file = e.target.files[0];
		if (file) {
			const reader = new FileReader();
			reader.onload = function () {
				const result = reader.result;
				setImageSrc(result);
				handleFunction(result);
				wrapperRef.current.classList.add("active");
			};
			reader.readAsDataURL(file);
		}
		if (e.target.value) {
			let valueStore = e.target.value.match(regExp);
			fileRef.current.innerHTML = valueStore;
		}
	}

	function handleCustomBtn(e) {
		defaultBtnRef.current.click();
	}

	return (
		<div className='inner-container'>
			<div className='wrapper-container' ref={wrapperRef}>
				<div className='image'>
					<img src={imageSrc} alt='' />
				</div>
				<div className='content'>
					<div className='icon'>
						<img src='/images/cloud-arrow-up-solid.svg' alt='cloud-icon' />
					</div>
					<div className='text'>No file Choosen</div>
				</div>
				<div id='cancel-btn'>
					<img src='/images/circle-xmark-solid.svg' alt='cross-btn' />
				</div>
				<div className='file-name' ref={fileRef}>
					File name Here
				</div>
			</div>
			<input
				id='default-btn'
				type='file'
				hidden
				onChange={handleDefaultClick}
				ref={defaultBtnRef}
			/>
			<Button
				id='custom-btn'
				name='Choose a File'
				handleFunction={handleCustomBtn}
			/>
			{props.children}
		</div>
	);
};

export default ImageUpload;
