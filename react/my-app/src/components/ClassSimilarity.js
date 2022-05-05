import React from "react";
import HorizontalChart from "./HorizontalChart";

const ClassSimilarity = (props) => {
	return (
		<div className='item class-sim'>
			<div className='heading'>Class Similarity</div>
			<div className='horizontal-chart'>
				{props.data.map((data, key) => {
					return (
						<HorizontalChart
							label={data.class}
							percent={data.percent}
							key={key}
						/>
					);
				})}
			</div>
		</div>
	);
};

export default ClassSimilarity;
