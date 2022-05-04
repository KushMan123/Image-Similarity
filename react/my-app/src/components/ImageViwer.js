import React from "react";

const ImageViewer = (props) => {
	return (
		<div className='item photo'>
			<div className='wrapper main-image'>
				<div className='image'>
					<img src={props.imageSrc} alt=' ' />
				</div>
				<div className='animal-name'>{props.animalName}</div>
			</div>
		</div>
	);
};

export default ImageViewer;
