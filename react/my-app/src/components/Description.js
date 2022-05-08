import React, { useState, useEffect, Fragment } from "react";
import Loading from "./Loading";

const Description = (props) => {
	const [responseData, setResponseData] = useState([]);
	const [jsonData, setJsonData] = useState([]);

	useEffect(() => {
		const fetchData = async () => {
			const response = await fetch(
				`http://127.0.0.1:8000/api/animal/${props.animalName}`
			);
			const json = await response.json();
			setJsonData(json);
		};
		fetchData().catch(console.error);
	}, []);

	useEffect(() => {
		console.log(jsonData);
		if (jsonData !== undefined && jsonData.length !== 0) {
			const data = {
				description: jsonData.description,
				status: jsonData.conservation_status.status,
			};
			setResponseData(data);
		}
	}, [jsonData]);

	function RenderContent() {
		if (responseData.length === 0) {
			return (
				<div className='item description'>
					<Loading LoadingText='Fetching Description' />
				</div>
			);
		} else {
			return (
				<div className='item description'>
					<div className='heading'>Description</div>
					<div className='content'>{responseData.description}</div>
					<div className='conservation'>
						Conservation Status: <span>{responseData.status}</span>
					</div>
				</div>
			);
		}
	}

	return <Fragment>{RenderContent()}</Fragment>;
};

export default Description;
