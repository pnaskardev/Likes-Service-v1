package main

import (
	"fmt"

	"github.com/pnaskardev/Likes-Service-v1/core/config"
)

func main() {
	cfg, err := config.LoadConfig()
	if err != nil {
		panic(err)
	}

	fmt.Println(cfg.Port)

}
