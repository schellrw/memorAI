import React from 'react';
import MnemonicForm from './components/MnemonicForm';
import MnemonicResult from './components/MnemonicResult';
import './App.css';

function App() {
  const [mnemonic, setMnemonic] = React.useState('');

  const handleMnemonicGeneration = (generatedMnemonic) => {
    setMnemonic(generatedMnemonic);
  };

  return (
    <div className="App">
      <h1>Mnemonic Device Generator</h1>
      <MnemonicForm onMnemonicGenerated={handleMnemonicGeneration} />
      <MnemonicResult mnemonic={mnemonic} />
    </div>
  );
}

export default App;