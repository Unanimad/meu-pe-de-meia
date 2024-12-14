'use client';
import React from 'react';
import { Tabs } from '@mantine/core';
import HomeSliders from '@/components/HomeSliders';
import LoginForm from '@/components/LoginForm';

export default function Home() {
  return (
    <div className="flex h-screen">
      <div className="w-1/2 flex items-center justify-center bg-gray-100">
        <HomeSliders />
      </div>
      <div className="w-1/2 flex items-center justify-center">
        <Tabs defaultValue="Login">
          <Tabs.List>
            <Tabs.Tab value="Login">Meu Pé-de-meia</Tabs.Tab>
            <Tabs.Tab value="Sobre-Programa">Sobre o programa</Tabs.Tab>
          </Tabs.List>
          <Tabs.Panel value="Login">
            <LoginForm />
          </Tabs.Panel>
        </Tabs>
      </div>
    </div>
  );
}
