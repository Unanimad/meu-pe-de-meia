import { MantineProvider } from '@mantine/core';
import '@mantine/core/styles.css';
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export const metadata = {
  title: "Meu Pé-de-meia",
  description: "",
};

export default function RootLayout({ children }) {
  return (
    <html lang="pt-br">
      <body className="antialiased text-gray-600">
        <MantineProvider withGlobalStyles withNormalizeCSS>
          <Header />
          {children}
          <Footer />
        </MantineProvider>
      </body>
    </html>
  );
}