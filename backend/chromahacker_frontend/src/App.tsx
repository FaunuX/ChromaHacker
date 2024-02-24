import { useState } from 'react'

import './App.css'
import { CustomColors } from './ColorInputs.tsx'

import '@blueprintjs/core/lib/css/blueprint.css';
import { Card, Elevation, InputGroup, FormGroup, RadioGroup, Radio, Collapse, Divider, Button, Icon } from '@blueprintjs/core'

const App = () => {
	const [formOption, setFormOption] = useState("use_colorscheme")
	const [colorscheme, setColorscheme] = useState("")
	const [customColors, setCustomColors] = useState([])
	const [imageUrl, setImageUrl] = useState("")
	const [url, setUrl] = useState("")
	const [outputUrl, setOutputUrl] = useState("")

	const submitForm = (_event: any) => {
		let fetchUrl = "";
		if (formOption === "use_colorscheme") {
			fetchUrl = "/palettize_premade?url=" + url + "&palette=" + colorscheme;
		} else if (formOption === "custom_colors") {
			let customColorsString = "";
			let i = 0;
			console.log(customColors)
			customColors.forEach(color => {
				customColorsString += "&arg" + i.toString() + "=" + color['value'];
				i += 1;
			});
			fetchUrl = "/palettize_custom?&url=" + url + customColorsString.replace(/#/g, "%23");
		} else if (formOption === "from_image") {
			fetchUrl = "/palettize_from_image?url=" + url + "&url_colors=" + imageUrl;
		};
		setOutputUrl(fetchUrl);
	};

	return (
			<>
			<Card interactive={ false } elevation={Elevation.ZERO} className="flex justify-center h-full m-16 rounded-xl bg-stone-800/40 blurry">
			<FormGroup className="w-1/2 min-w-max" >
			<Card interactive={ true } elevation={Elevation.ZERO} className="rounded-xl text-stone-50 bg-stone-900/40 blurry">
			<RadioGroup 
				onChange={ (event: any) => setFormOption(event.currentTarget.value) }
				selectedValue={ formOption }
			>
			<Radio value="use_colorscheme">
				<strong className="text-xl"> <Icon icon="geosearch" /> Use Colorscheme </strong>
			</Radio>
			<Collapse isOpen={ formOption === "use_colorscheme" }> 
				<InputGroup 
					name="colorscheme" 
					type="search" 
					placeholder="Search?" 
					leftIcon="search"
					className="ml-8 bp5-dark"
					onChange={ (event) => setColorscheme(event.target.value) }
				/>
			</Collapse>
			<Radio value="custom_colors">
				<strong className="text-xl"> <Icon icon="style" /> Custom Colors </strong>
			</Radio>
			<Collapse isOpen={ formOption === "custom_colors" }> 
				<CustomColors onChange={(event: any) => {
					setCustomColors(event.target.value)} 
				}
				/>
			</Collapse>
			<Radio value="from_image">
				<strong className="text-xl"> <Icon icon="media" /> From Image </strong>
			</Radio>
			<Collapse isOpen={ formOption === "from_image" }> 
				<InputGroup 
					name="color_image_url" 
					type="url" 
					placeholder="Enter URL for your Image"
					className="ml-8 bp5-dark"
					onChange={ (event: any) => setImageUrl(event.target.value) }
				/>
			</Collapse>
			</RadioGroup>
			</Card>

			<Divider className="invisible" />
			<InputGroup 
				name="image_url" 
				type="url" 
				placeholder="Enter the URL for the image you wish to recolor..." 
				onChange={ (event: any) => setUrl(event.target.value) }
				className="bp5-dark"
			/>
			<Divider className="invisible"/>
			<div className="bp5-dark">
			<Button onClick={ submitForm }> Submit </Button>
			</div>
			</FormGroup>
			</Card>
			<center>
			<img className="w-1/2" src={outputUrl} />
			<br />
			</center>
			</>
	       )
}

export default App
