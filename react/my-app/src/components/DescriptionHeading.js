import React from "react";

const DescriptionHeading = (props) => {
	return (
		<div className={props.class}>
			<div className='heading'>{props.title}</div>
			{props.children}
		</div>
	);
};

export default DescriptionHeading;
