import React from "react";
import HorizontalChart from "./HorizontalChart";

const ClassSimilarity = (props) => {
	return (
		<div className='item class-sim'>
			<div className='heading'>Class Similarity</div>
			<div className='horizontal-chart'>
				{props.data.map((data, key) => {
					console.log(data);
					return (
						<HorizontalChart
							label={data.class}
							percent={parseInt(data.percent)}
							key={key}
						/>
					);
				})}
			</div>
		</div>
	);
};

export default ClassSimilarity;
