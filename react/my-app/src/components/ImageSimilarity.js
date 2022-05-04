import React, { useEffect, useState } from "react";
import { Fragment } from "react";
import RelatedImage from "./RelatedImage";
import DataJson from "../response.json";
import Loading from "./Loading";

const ImageSimilarity = (props) => {
	const [responseData, setResponseData] = useState([]);

	useEffect(() => {
		setTimeout(() => {
			setResponseData(DataJson[0]["Image-Similarity"]);
			console.log(responseData);
		}, 7000);
	});

	function RenderContent() {
		if (responseData.length === 0) {
			return (
				<div className='item loading-item'>
					<Loading LoadingText='Searching Related Images' />
				</div>
			);
		} else {
			return (
				<Fragment>
					{responseData.map((data, index) => {
						return (
							<RelatedImage
								id={`image${index + 1}`}
								imageSrc={data.imageSrc}
								name={`Image${index + 1}`}
								percent={data.percent}
								gradientid={`GradientColor${index + 1}`}
								circleid={`circle${index + 1}`}
								key={index}
							/>
						);
					})}
				</Fragment>
			);
		}
	}

	return (
		<Fragment>
			{RenderContent()}
			{/* {props.data.map((data, index) => {
				return (
					<RelatedImage
						id={`image${index + 1}`}
						imageSrc={data.imageSrc}
						name={`Image${index + 1}`}
						percent={data.percent}
						gradientid={`GradientColor${index + 1}`}
						circleid={`circle${index + 1}`}
						key={index}
					/>
				);
			})} */}
		</Fragment>
	);
};

export default ImageSimilarity;
