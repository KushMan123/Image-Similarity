import React from "react";

const Description = (props) => {
	return (
		<div className='item description'>
			<div className='heading'>Description</div>
			<div className='content'>{props.detail}</div>
		</div>
	);
};

export default Description;
