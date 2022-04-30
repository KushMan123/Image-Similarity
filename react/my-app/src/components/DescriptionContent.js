import React from "react";

const DescriptionContent = (props) => {
	return (
		<div className='content'>
			<span className='highlight'>{props.label}</span>
			<div>{props.value}</div>
		</div>
	);
};

export default DescriptionContent;
