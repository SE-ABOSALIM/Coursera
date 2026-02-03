/* Render Props Advanced Example */
import { useState } from "react";

type FormHandlerProps = {
  render: Function;
};

const FormHandler = ({ render }: FormHandlerProps) => {
  const [formData, setFormData] = useState({});
  const [error, setError] = useState({});

  const handleChange = (e: React.FormEvent<HTMLFormElement>) => {
    const { name, value, type } = e.currentTarget;
    if (value === "") setError({ msg: `${name} is required` });
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    let formData = new FormData(e.currentTarget);
    let formDataObj = Object.fromEntries(formData.entries());
    setFormData(formDataObj);
    console.log(formDataObj);
  };

  return render({ formData, error, handleChange, handleSubmit });
};

export default FormHandler;
