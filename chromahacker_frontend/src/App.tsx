import { useState, useEffect, useRef } from 'react'

import './App.css'
import { CustomColors, FromImage } from './ColorInputs.tsx'

import '@blueprintjs/core/lib/css/blueprint.css';
import { Card, Elevation, ControlGroup, InputGroup, FormGroup, RadioGroup, Radio, Collapse, Divider, Button, Icon, Iconsize } from '@blueprintjs/core'

const App = () => {
	const [formOption, setFormOption] = useState("use_colorscheme")
	const [colorscheme, setColorscheme] = useState("")
	const [customColors, setCustomColors] = useState([])
	const [imageUrl, setImageUrl] = useState("")
	const [url, setUrl] = useState("")

	const submitForm = (event) => {
		console.log({formOption: formOption, colorscheme: colorscheme, customColors: customColors, imageUrl: imageUrl})
		let fetchUrl = ""
		console.log(imageUrl)
		if (formOption === "use_colorscheme") {
			fetchUrl = "http://localhost:5000/palettize_premade?url=" + url + "&palette=" + colorscheme
			fetch(fetchUrl, {})
		} else if (formOption === "custom_colors") {
			fetchUrl = "/palettize_custom"
		} else if (formOption === "from_image") {
			fetchUrl = "/palettize_from_image"
		}
	}

	return (
			<Card interactive={ false } elevation={Elevation.TWO} className="flex justify-center h-full m-16">
			<FormGroup large={ true } className="w-1/2 min-w-max" >
			<Card interactive={ true } elevation={Elevation.TWO} className="">
			<RadioGroup 
				onChange={ (event) => setFormOption(event.currentTarget.value) }
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
					className="ml-8"
					onChange={ (event) => setColorscheme(event.target.value) }
				/>
			</Collapse>
			<Radio value="custom_colors">
				<strong className="text-xl"> <Icon icon="style" /> Custom Colors </strong>
			</Radio>
			<Collapse isOpen={ formOption === "custom_colors" }> 
				<CustomColors onChange={(event) => {
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
					className="ml-8"
					onChange={ (event) => setImageUrl(event.target.value) }
				/>
			</Collapse>
			</RadioGroup>
			</Card>

			<Divider className="invisible" />
			<InputGroup 
				name="image_url" 
				type="url" 
				placeholder="Enter the URL for the image you wish to recolor..." 
				onChange={ (event) => setUrl(event.target.value) }
			/>
			<Divider className="invisible"/>
			<Button onClick={ submitForm }> Submit </Button>
			</FormGroup>
			</Card>
	       )
}

export default App
