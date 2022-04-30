import React, { useRef } from "react";

function changeChartNumber(percent, number) {
	let valueNumber = parseInt(472 - (472 * percent) / 100);
	let counter = 0;
	document.documentElement.style.setProperty("--end-dashstroke", valueNumber);
	setInterval(() => {
		if (counter === percent) {
			clearInterval();
		} else {
			counter += 1;
			number.current.innerHTML = `${counter}%`;
		}
	}, 30);
}

const RelatedImage = (props) => {
	const number = useRef();

	return (
		<div
			className='item image-sim'
			id={props.id}
			onMouseEnter={() => {
				let percent = parseInt(number.current.dataset.percent);
				changeChartNumber(percent, number);
			}}>
			<div className='wrapper related-image'>
				<div className='image'>
					<img src={props.imageSrc} alt='related-img' id='related-image' />
				</div>
				<div className='animal-name'>{props.name}</div>
			</div>
			<div className='circular-chart'>
				<div className='chart-wrapper'>
					<div className='outer-circle'>
						<div className='inner-circle'>
							<div
								className='number'
								data-percent={props.percent}
								ref={number}></div>
						</div>
					</div>
					<svg
						xmlns='http://www.w3.org/2000/svg'
						version='1.1'
						width='160px'
						height='160px'>
						<defs>
							<linearGradient id={props.gradientid}>
								<stop offset='0%' stopColor='#3a8ffe' />
								<stop offset='100%' stopColor='#9658fe' />
							</linearGradient>
						</defs>
						<circle
							cx='80'
							cy='80'
							r='70'
							strokeLinecap='round'
							id={props.circleid}
						/>
					</svg>
				</div>
			</div>
		</div>
	);
};

export default RelatedImage;
