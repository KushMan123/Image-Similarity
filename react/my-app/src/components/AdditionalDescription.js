import React, { Fragment, useEffect, useState } from "react";
import DescriptionContent from "./DescriptionContent";
import DescriptionHeading from "./DescriptionHeading";
import Loading from "./Loading";

const AdditionalDescription = () => {
	const [responseData, setResponseData] = useState([]);
	const [jsonData, setJsonData] = useState([]);

	useEffect(() => {
		const fetchData = async () => {
			const response = await fetch("http://127.0.0.1:8000/api/animals/");
			const json = await response.json();
			setJsonData(json[0]);
		};
		fetchData().catch(console.error);
	}, []);

	useEffect(() => {
		console.log(jsonData);
		if (jsonData !== undefined && jsonData.length !== 0) {
			const additionalDescription = {
				Scientific: [],
				Physical: [],
				Facts: [],
				Location: [],
				"Location Image": "",
			};
			additionalDescription.Scientific = transformResponse(
				jsonData.classification,
				true
			);
			additionalDescription.Physical = transformResponse(
				jsonData.physical_characteristics,
				false
			);
			additionalDescription.Facts = transformResponse(jsonData.facts, false);
			for (let i = 0; i < jsonData.location.length; i++) {
				additionalDescription.Location.push(jsonData.location[i].name);
			}
			setResponseData(additionalDescription);
		}
	}, [jsonData]);

	function transformResponse(object, hasName) {
		const label = Object.keys(object);
		let dataValue = [];
		let value = null;
		for (let i = 1; i < label.length; i++) {
			const str = label[i].split("_").join(" ");
			if (hasName) {
				value = object[label[i]].name;
			} else {
				value = object[label[i]];
			}
			if (value !== null) {
				const data = {
					label: str.charAt(0).toUpperCase() + str.slice(1),
					value: value,
				};
				dataValue.push(data);
			}
		}
		return dataValue;
	}

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
