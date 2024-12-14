import React, { useState } from 'react';
import Modal from '@/components/Modal';

const LoginForm = () => {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errors, setErrors] = useState({});
    const [isCheckboxChecked, setIsCheckboxChecked] = useState(false);

    const openModal = (e) => {
        e.preventDefault();
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    const handleCheckboxChange = (e) => {
        setIsCheckboxChecked(e.target.checked);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const newErrors = {};

        if (!username) {
            newErrors.username = 'O campo é obrigatório';
        }

        if (!password) {
            newErrors.password = 'O campo é obrigatório';
        }

        if (!isCheckboxChecked) {
            newErrors.checked = 'Você precisa ler sobre a plataforma';
        }

        if (Object.keys(newErrors).length > 0) {
            setErrors(newErrors);
        } else {
            // Submit the form
        }
    };


    return (
        <>
            <Modal isOpen={isModalOpen} onClose={closeModal} title="Sobre a Plataforma">
                <p>
                    Esta plataforma, Meu Pé-de-meia, é um sistema para ajudar os discentes a tirar dúvida sobre seu incentivo.
                </p>
            </Modal>

            <form className="bg-white p-8 rounded shadow-md w-full max-w-md" onSubmit={handleSubmit}>
                <h2 className="text-2xl font-bold mb-6">Meu Pé-de-meia</h2>
                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
                        Meu login Sigaa
                    </label>
                    <input
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        id="username"
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                    {errors.username && <p className="text-red-500 text-xs italic">{errors.username}</p>}
                </div>
                <div className="mb-6">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
                        Minha senha Sigaa
                    </label>
                    <input
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        id="password"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    {errors.password && <p className="text-red-500 text-xs italic">{errors.password}</p>}
                </div>
                <div className="mb-4">
                    <input
                        type="checkbox"
                        id="readAboutPlatform"
                        className="mr-2 leading-tight"
                        onChange={handleCheckboxChange}
                    />
                    <label htmlFor="readAboutPlatform" className="text-gray-700 text-sm">
                        Eu li sobre <a href="#" onClick={openModal} className="text-blue-500">o que é a plataforma.</a>
                    </label>
                    {errors.checked && <p className="text-red-500 text-xs italic">{errors.checked}</p>}
                </div>
                <div className="mb-4">
                    <button
                        type="submit"
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    >
                        Acessar
                    </button>
                </div>
            </form>
        </>
    );
};

export default LoginForm;
