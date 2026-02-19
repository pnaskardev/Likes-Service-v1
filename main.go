package main

import (
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/middleware/recover"
	"github.com/pnaskardev/Likes-Service-v1/core/config"
)

func main() {
	cfg, err := config.LoadConfig()
	if err != nil {
		panic(err)
	}
	fiberConfig := fiber.Config{AppName: "Likes-Service-V2-CORE", CaseSensitive: true}
	app := fiber.New(fiberConfig)
	app.Use(recover.New())

	app.Use(func(c fiber.Ctx) error {
		start := time.Now()
		err := c.Next()
		duration := time.Since(start)
		c.Append("Server-Timing", "app;dur="+duration.String())
		return err
	})

	app.Get("/", func(c fiber.Ctx) error {
		return c.SendString("Hello, World!")
	})

	// Server starts on a go routine
	go func() {
		port := ":" + cfg.Port
		fiberListenConfig := fiber.ListenConfig{
			EnablePrefork:     true,
			EnablePrintRoutes: true,
		}
		log.Fatal(app.Listen(port, fiberListenConfig))
	}()

	// Graceful shutdown happens on the main thread and senses for the SIGTERM syscall
	c := make(chan os.Signal, 1)                    // Create channel to signify a signal being sent
	signal.Notify(c, os.Interrupt, syscall.SIGTERM) // When an interrupt or termination signal is sent, notify the channel

	_ = <-c // This blocks the main thread until an interrupt is received
	fmt.Println("Gracefully shutting down...")
	_ = app.Shutdown()

	fmt.Println("Running cleanup tasks...")

	// Your cleanup tasks go here
	// db.Close()
	// redisConn.Close()
	fmt.Println("Server was successful shutdown.")
}
