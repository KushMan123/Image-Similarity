import React from "react";

const Button = (props) => {
	return (
		<button className='button' onClick={props.handleFunction} id={props.id}>
			{props.name}
		</button>
	);
};

export default Button;
