import React from "react";
import HorizontalChart from "./HorizontalChart";

const ClassSimilarity = (props) => {
	return (
		<div className='item class-sim'>
			<div className='heading'>Class Similarity</div>
			<div className='horizontal-chart'>
				{props.data.map((data, key) => {
					console.log(data);
					if (data.percent < 0.1) {
						data.percent = data.percent * 100 + 20;
					}
					if (data.percent < 10) {
						data.percent = data.percent + 20;
					}
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
