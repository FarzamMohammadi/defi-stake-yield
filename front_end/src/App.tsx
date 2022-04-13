import React from 'react';
import { DAppProvider, Kovan, Rinkeby } from '@usedapp/core';
import { Header } from './components/layout/Header';
import { Main } from './components/main/Main';
import { Container } from '@material-ui/core';

function App() {
  return (
    <DAppProvider
      config={{
        networks: [Kovan],
        notifications: {
          expirationPeriod: 1000,
          checkInterval: 1000,
        },
      }}
    >
      <Header />
      <Container maxWidth='md'>
        <Main />
      </Container>
    </DAppProvider>
  );
}
export default App;
