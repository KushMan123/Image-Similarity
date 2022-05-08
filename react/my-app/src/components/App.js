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
import axios from "axios";

const response = DataJson[0];

const App = () => {
	const [imageSrc, setImageSrc] = useState("");
	const [isLoading, setisLoading] = useState(false);
	const [responseData, setResponseData] = useState([]);
	const [imageUploadStatus, setImageUploadStatus] = useState(false);
	const [selectedFile, setSelectedFile] = useState(null);
	const [animalName, setAnimalName] = useState("");

	function fileHandler(file) {
		console.log(file);
		setSelectedFile(file);
	}

	function handleImageSrc(newValue) {
		setImageSrc(newValue);
	}

	function handleImageUploadStatus(newValue) {
		setImageUploadStatus(newValue);
	}

	function handleModelClick(e) {
		console.log(imageUploadStatus);
		if (imageUploadStatus) {
			setisLoading(true);
			const body = new FormData();
			body.append("file", selectedFile);
			axios.post("http://127.0.0.1:8000/api/animalimage/", body).then((res) => {
				const classLabel = Object.keys(res.data);
				setAnimalName(classLabel[0]);
				const similartyPercent = [];
				for (let i = 0; i < classLabel.length; i++) {
					let data = {
						class: classLabel[i],
						percent: res.data[classLabel[i]]*100,
					};
					similartyPercent.push(data);
				}
				setResponseData(similartyPercent)
				setisLoading(false)
			});
		}
	}

	function RenderContent() {
		if (!isLoading && responseData.length === 0) {
			return (
				<OuterContainer>
					<ImageUpload
						handleFunction={handleImageSrc}
						handleStatus={handleImageUploadStatus}
						handleFile={fileHandler}>
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
						<ImageViewer imageSrc={imageSrc} animalName={animalName} />
						<AdditionalDescription animalName={animalName}/>
						<Description
							// detail={responseData.description}
							// status={responseData.conservation_status.status}
							animalName={animalName}
						/>
						<ClassSimilarity data={responseData} />
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
