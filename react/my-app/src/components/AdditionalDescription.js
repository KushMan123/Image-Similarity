import React, { Fragment, useEffect, useState } from "react";
import DescriptionContent from "./DescriptionContent";
import DescriptionHeading from "./DescriptionHeading";
import Loading from "./Loading";
import DataJson from "../response.json";

const AdditionalDescription = (props) => {
	const [responseData, setResponseData] = useState([]);

	useEffect(() => {
		setTimeout(() => {
			setResponseData(DataJson[0]["additional-description"]);
			console.log(responseData);
		}, 5000);
	}, [responseData]);

	function RenderContent() {
		if (responseData.length === 0) {
			return (
				<div className='item add-description'>
					<Loading LoadingText='Fetching Additional Information' />
				</div>
			);
		} else {
			return (
				<div className='item add-description'>
					<div className='heading'>Additional Information</div>
					<div className='category'>
						<div className='row'>
							<DescriptionHeading
								class='scientific'
								title='Scientific Classification'>
								{responseData.Scientific.map((content, key) => {
									return (
										<DescriptionContent
											label={content.label}
											value={content.value}
											key={key}
										/>
									);
								})}
							</DescriptionHeading>
							<DescriptionHeading
								class='physical'
								title='Physical Characteristics'>
								{responseData.Physical.map((content, key) => {
									return (
										<DescriptionContent
											label={content.label}
											value={content.value}
											key={key}
										/>
									);
								})}
							</DescriptionHeading>
						</div>
						<div className='row'>
							<DescriptionHeading class='facts' title='Facts'>
								{responseData.Facts.map((content, key) => {
									return (
										<DescriptionContent
											label={content.label}
											value={content.value}
											key={key}
										/>
									);
								})}
							</DescriptionHeading>
							<DescriptionHeading class='location' title='Locations'>
								<div class='row'>
									<div class='col'>
										{responseData.Location.map((content, key) => {
											if (key % 2 !== 0) {
												return (
													<div className='content' key={key}>
														{content}
													</div>
												);
											}
										})}
									</div>
									<div class='col'>
										{responseData.Location.map((content, key) => {
											if (key % 2 === 0) {
												return (
													<div className='content' key={key}>
														{content}
													</div>
												);
											}
										})}
									</div>
								</div>
								<div class='image'>
									<img src={responseData["Location Image"]} />
								</div>
							</DescriptionHeading>
						</div>
					</div>
				</div>
			);
		}
	}

	return <Fragment>{RenderContent()}</Fragment>;
};

export default AdditionalDescription;
