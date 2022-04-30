import React, { useEffect, useRef } from "react";

const HorizontalChart = (props) => {
	const barInner = useRef();

	useEffect(() => {
		barInner.current.style.width = barInner.current.dataset.percent;
	});

	return (
		<div className='chart'>
			<div className='bar-title'>{props.label}</div>
			<div className='bar'>
				<div
					className='bar-inner'
					data-percent={`${props.percent}%`}
					ref={barInner}></div>
			</div>
		</div>
	);
};

export default HorizontalChart;
