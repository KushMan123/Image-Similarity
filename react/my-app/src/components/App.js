import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import "../static/css/style.css";
import ImageViewer from "./ImageViwer";
import AdditionalDescription from "./AdditionalDescription";
import GridContainer from "../container/GridContainer";
import DataJson from "../response.json";
import Description from "./Description";
import ClassSimilarity from "./ClassSimilarity";
import ImageSimilarity from "./ImageSimilarity";
import OuterContainer from "../container/OuterContainer";
import { Fragment } from "react";
import ImageUpload from "./ImageUpload";
import Button from "./Button";
import Loading from "./Loading";

const response = DataJson[0];

const App = () => {
	const [imageSrc, setImageSrc] = useState("");
	const [isLoading, setisLoading] = useState(false);
	const [responseData, setResponseData] = useState([]);
	const [imageUploadStatus, setImageUploadStatus] = useState(false);

	function handleImageSrc(newValue) {
		console.log(newValue);
		setImageSrc(newValue);
		console.log("Image Src", imageSrc);
	}

	function handleImageUploadStatus(newValue) {
		console.log(newValue);
		setImageUploadStatus(newValue);
		console.log("Status", newValue);
	}

	function handleModelClick(e) {
		console.log(imageUploadStatus);
		if (imageUploadStatus) {
			setisLoading(true);
			fetch("http://127.0.0.1:8000/api/animals/")
				.then((response) => response.json())
				.then((data) => {
					console.log(data[0]);
					setResponseData(data[0]);
					setisLoading(false);
				});
			// setTimeout(() => {
			// 	setResponseData(response);
			// 	setisLoading(false);
			// }, 5000);
		}
	}

	function RenderContent() {
		if (!isLoading && responseData.length === 0) {
			return (
				<OuterContainer>
					<ImageUpload
						handleFunction={handleImageSrc}
						handleStatus={handleImageUploadStatus}>
						<Button
							id='model-btn'
							name='Get my Animal'
							handleFunction={handleModelClick}
						/>
					</ImageUpload>
				</OuterContainer>
			);
		} else {
			if (isLoading) {
				return (
					<OuterContainer>
						<Loading LoadingText='Loading' />
					</OuterContainer>
				);
			} else {
				return (
					<GridContainer>
						<ImageViewer imageSrc={imageSrc} animalName={responseData.name} />
						<AdditionalDescription />
						<Description
							detail={responseData.description}
							status={responseData.conservation_status.status}
						/>
						<ClassSimilarity data={response["Class-Similarity"]} />
						<ImageSimilarity data={response["Image-Similarity"]} />
					</GridContainer>
				);
			}
		}
	}

	return <Fragment>{RenderContent()}</Fragment>;
};

const root = ReactDOM.createRoot(document.querySelector("#root"));
root.render(<App />);
